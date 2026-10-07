/**
 * RetailSync WMS - Swiss Minimalist Overview Client Script
 * Implements accessible interactions, count-up animation, role filtering, and theme switching.
 */

(function () {
  'use strict';

  // 1. Theme Toggle Controller
  window.toggleTheme = function () {
    const currentTheme = document.documentElement.getAttribute('data-theme') || (document.documentElement.classList.contains('dark') ? 'dark' : 'light');
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nextTheme);
    if (nextTheme === 'dark') {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    try {
      localStorage.setItem('retailsync-theme', nextTheme);
    } catch (e) {
      /* ignore local storage error */
    }
  };

  // 2. Valuation Metric Count-up Animation
  function initValuationCountUp() {
    const el = document.getElementById('metricValuation');
    if (!el) return;

    const rawTarget = parseFloat(el.getAttribute('data-target') || '0');
    if (isNaN(rawTarget) || rawTarget <= 0) return;

    // Respect user's motion preference
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      el.innerHTML = '<span class="status-strip__currency">৳</span>' + rawTarget.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
      return;
    }

    const duration = 1200; // ms
    const startTime = performance.now();

    function easeOutQuad(t) {
      return t * (2 - t);
    }

    function step(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1.0);
      const currentVal = easeOutQuad(progress) * rawTarget;

      el.innerHTML = '<span class="status-strip__currency">৳</span>' + currentVal.toLocaleString('en-US', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
      });

      if (progress < 1.0) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }

  // 3. Accessible Dropdown Menu
  function initDropdown() {
    const trigger = document.getElementById('moreNavBtn');
    const menu = document.getElementById('moreNavMenu');
    if (!trigger || !menu) return;

    function openDropdown() {
      trigger.setAttribute('aria-expanded', 'true');
      menu.classList.add('dropdown__menu--open');
    }

    function closeDropdown() {
      trigger.setAttribute('aria-expanded', 'false');
      menu.classList.remove('dropdown__menu--open');
    }

    trigger.addEventListener('click', function (e) {
      e.stopPropagation();
      const isOpen = trigger.getAttribute('aria-expanded') === 'true';
      if (isOpen) {
        closeDropdown();
      } else {
        openDropdown();
      }
    });

    document.addEventListener('click', function (e) {
      if (!trigger.contains(e.target) && !menu.contains(e.target)) {
        closeDropdown();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && trigger.getAttribute('aria-expanded') === 'true') {
        closeDropdown();
        trigger.focus();
      }
    });
  }

  // 4. Mobile Drawer Controller
  function initMobileDrawer() {
    const menuBtn = document.getElementById('mobileMenuBtn');
    const drawer = document.getElementById('mobileDrawer');
    const closeBtn = document.getElementById('mobileDrawerClose');
    if (!menuBtn || !drawer) return;

    function openDrawer() {
      menuBtn.setAttribute('aria-expanded', 'true');
      drawer.classList.add('mobile-drawer--open');
      drawer.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      menuBtn.setAttribute('aria-expanded', 'false');
      drawer.classList.remove('mobile-drawer--open');
      drawer.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    menuBtn.addEventListener('click', function () {
      const isOpen = menuBtn.getAttribute('aria-expanded') === 'true';
      if (isOpen) closeDrawer();
      else openDrawer();
    });

    if (closeBtn) {
      closeBtn.addEventListener('click', closeDrawer);
    }

    drawer.addEventListener('click', function (e) {
      if (e.target === drawer) closeDrawer();
    });
  }

  // 5. Role Switcher Reactive Reordering
  const ROLE_MAP = {
    admin: { label: 'Director (All)', primary: 'pos' },
    cashier: { label: 'Cashier', primary: 'pos' },
    clerk: { label: 'Dock Clerk', primary: 'inbound' },
    operator: { label: 'Floor Operator', primary: 'putaway' },
    supervisor: { label: 'Supervisor', primary: 'warehouse' },
    procurement: { label: 'SCM Officer', primary: 'procurement' }
  };

  window.reorderWorkspacesByRole = function (role) {
    const grid = document.getElementById('workspacesGrid');
    const indicator = document.getElementById('activeRoleIndicator');
    if (!grid) return;

    try {
      localStorage.setItem('retailsync-active-role', role);
    } catch (e) {}

    const config = ROLE_MAP[role] || ROLE_MAP.admin;
    if (indicator) {
      indicator.textContent = 'Role: ' + config.label;
    }

    // Select the switcher if not synchronized
    const select = document.getElementById('roleSwitcherSelect');
    if (select && select.value !== role) {
      select.value = role;
    }

    // Reorder workspaces
    const rows = Array.from(grid.querySelectorAll('.workspace-row'));
    rows.forEach(function (row) {
      row.classList.remove('workspace-row--primary');
    });

    const primaryRow = grid.querySelector('[data-priority-role="' + role + '"]') ||
                       grid.querySelector('[data-module="' + config.primary + '"]');

    if (primaryRow) {
      primaryRow.classList.add('workspace-row--primary');
      grid.prepend(primaryRow);
    }

    // Renumber rows sequentially
    const updatedRows = Array.from(grid.querySelectorAll('.workspace-row'));
    updatedRows.forEach(function (row, idx) {
      const numEl = row.querySelector('.workspace-row__num');
      if (numEl) {
        numEl.textContent = String(idx + 1).padStart(2, '0');
      }
    });

    // Reorder Attention rows
    const attentionList = document.getElementById('attentionList');
    if (attentionList) {
      const attRows = Array.from(attentionList.querySelectorAll('.attention-row'));
      attRows.forEach(function (attRow) {
        const itemRole = attRow.getAttribute('data-role');
        if (role === 'admin' || !itemRole || itemRole === role) {
          attRow.style.display = 'grid';
        } else {
          attRow.style.display = 'grid'; // Keep visible in ruled list but lower visual weight
        }
      });
    }
  };

  window.switchRole = async function (role) {
    window.reorderWorkspacesByRole(role);
    try {
      const res = await fetch('/api/v1/auth/switch-role', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ role: role })
      });
      if (res.ok) {
        if (typeof showToast === 'function') {
          showToast(`Active persona switched to ${role.toUpperCase()}`, 'success', 'Persona Changed');
        }
        setTimeout(() => window.location.reload(), 300);
      }
    } catch (err) {
      console.warn('Role switch network request failed:', err);
    }
  };

  // 6. Keyboard Shortcuts
  function initKeyboardShortcuts() {
    document.addEventListener('keydown', function (e) {
      // Don't trigger when user is typing in inputs or selects
      const tag = (e.target.tagName || '').toLowerCase();
      if (tag === 'input' || tag === 'textarea' || tag === 'select' || e.metaKey || e.ctrlKey || e.altKey) {
        return;
      }

      const key = e.key.toUpperCase();
      const routes = {
        P: '/pos',
        I: '/inbound',
        U: '/putaway',
        W: '/warehouse',
        R: '/procurement',
        L: '/audits'
      };

      if (routes[key]) {
        e.preventDefault();
        window.location.href = routes[key];
      } else if (key === 'T') {
        e.preventDefault();
        window.toggleTheme();
      }
    });
  }

  // 7. Calm Mission Studio Cockpit Interactivity
  window.copyHashText = function (hash) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(hash).then(function () {
        if (typeof showToast === 'function') {
          showToast('Copied cryptographic hash: ' + hash, 'success', 'Audit Verified');
        }
      }).catch(function () {});
    }
  };

  window.switchStoreLocation = function (store) {
    const storeNames = {
      uttara: 'Uttara Central Super Shop',
      dhanmondi: 'Dhanmondi Express Hub',
      gulshan: 'Gulshan Mega Mart'
    };
    const name = storeNames[store] || store;
    try {
      localStorage.setItem('retailsync-active-store', store);
    } catch (e) {}
    if (typeof showToast === 'function') {
      showToast('Switched active telemetry node to ' + name, 'info', 'Store Synchronized');
    }
  };

  // Live Cryptographic Audit Stream Simulated Ingestion
  function initLiveAuditStream() {
    const container = document.getElementById('auditStreamContainer');
    if (!container) return;

    const sampleActions = ['POS_SALE', 'FEFO_SWEEP', 'DOCK_RECV', 'PUTAWAY'];
    const sampleHashes = [
      'd3f82b79a10c4f81b',
      'e89a31bc40ef1a72d',
      'c518be92376b757e3',
      'f47a192b83a379b32',
      'b817729363e4967ae'
    ];

    setInterval(function () {
      const now = new Date();
      const timeStr = String(now.getHours()).padStart(2, '0') + ':' +
                      String(now.getMinutes()).padStart(2, '0') + ':' +
                      String(now.getSeconds()).padStart(2, '0') + '.' +
                      String(now.getMilliseconds()).padStart(3, '0');

      const action = sampleActions[Math.floor(Math.random() * sampleActions.length)];
      const hashPart = sampleHashes[Math.floor(Math.random() * sampleHashes.length)];
      const fullHash = hashPart + Math.random().toString(16).substring(2, 10);

      const row = document.createElement('div');
      row.className = 'audit-stream-row';
      row.style.opacity = '0';
      row.style.transition = 'opacity 0.4s ease';

      row.innerHTML = '<div>' +
        '<span class="audit-action-chip">' + action + '</span> ' +
        '<span class="audit-stream-hash" title="Click to copy SHA-256 hash" onclick="copyHashText(\'' + fullHash + '\')">hash:' + hashPart.substring(0, 6) + '...</span>' +
      '</div>' +
      '<span class="tabular audit-stream-time">' + timeStr + '</span>';

      container.insertBefore(row, container.firstChild);
      requestAnimationFrame(function () {
        row.style.opacity = '1';
      });

      if (container.children.length > 8) {
        container.removeChild(container.lastChild);
      }
    }, 7000);
  }

  // Initialization on DOMContentLoaded
  document.addEventListener('DOMContentLoaded', function () {
    initValuationCountUp();
    initDropdown();
    initMobileDrawer();
    initKeyboardShortcuts();
    initLiveAuditStream();

    // Restore saved role
    try {
      const savedRole = localStorage.getItem('retailsync-active-role');
      if (savedRole && ROLE_MAP[savedRole]) {
        window.reorderWorkspacesByRole(savedRole);
      }
    } catch (e) {}

    // Restore saved store
    try {
      const savedStore = localStorage.getItem('retailsync-active-store');
      const storeSelect = document.getElementById('activeStoreSelect');
      if (savedStore && storeSelect) {
        storeSelect.value = savedStore;
      }
    } catch (e) {}
  });
})();

