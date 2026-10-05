/**
 * RetailSync Enterprise WMS - Unified Navigation & Telemetry System
 * Provides header dropdowns, mobile navigation, theme toggling, store switching, and role switching across all pages.
 */
(function () {
  'use strict';

  // 1. Theme Toggle Controller
  window.toggleTheme = function () {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', nextTheme);
    try {
      localStorage.setItem('retailsync-theme', nextTheme);
    } catch (e) {}
  };

  // 2. Accessible Dropdown Menu
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

  // 3. Mobile Navigation Drawer Controller
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

  // 4. Role Switcher
  window.switchRole = async function (role) {
    try {
      localStorage.setItem('retailsync-active-role', role);
    } catch (e) {}

    try {
      const res = await fetch('/api/v1/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username_or_email: role, password: 'Password123!' })
      });
      if (res.ok) {
        if (typeof showToast === 'function') {
          showToast(`Switched operational persona to ${role}`, 'success', 'Role Updated');
        }
      }
    } catch (err) {
      console.warn('Role switch endpoint unavailable:', err);
    }

    // Update switcher select elements
    const select = document.getElementById('roleSwitcherSelect');
    if (select && select.value !== role) {
      select.value = role;
    }
  };

  // 5. Store Location Switcher
  window.switchStoreLocation = function (store) {
    const storeNames = {
      uttara: 'Uttara Central Super Shop',
      dhanmondi: 'Dhanmondi Express Hub',
      gulshan: 'Gulshan Mega Mart'
    };
    try {
      localStorage.setItem('retailsync-active-store', store);
    } catch (e) {}

    if (typeof showToast === 'function') {
      showToast('Active Super Shop location: ' + (storeNames[store] || store), 'info', 'Store Switch');
    }
  };

  // 6. Global Toast Notifications
  window.showToast = function (message, type = 'info', title = '') {
    let container = document.getElementById('toastContainer');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toastContainer';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `toast-item toast-${type}`;

    const icon = type === 'success' ? '✓' : type === 'error' ? '✕' : 'ℹ';
    const iconColor = type === 'success' ? 'var(--color-status-success, #10b981)' : type === 'error' ? 'var(--color-status-danger, #ef4444)' : 'var(--color-accent, #38bdf8)';
    const defaultTitle = type === 'success' ? 'Operation Confirmed' : type === 'error' ? 'System Alert' : 'Operational Notice';
    const displayTitle = title || defaultTitle;

    toast.innerHTML = `
      <div class="toast-icon" style="color: ${iconColor}; font-weight: 700; font-family: var(--font-mono);">${icon}</div>
      <div class="toast-body">
        <div class="toast-title" style="font-weight: 600; font-size: 13px;">${displayTitle}</div>
        <div class="toast-message" style="font-size: 12px; color: var(--color-text-secondary);">${message}</div>
      </div>
      <button class="toast-close-btn" onclick="this.parentElement.remove()" title="Dismiss" style="background:none; border:none; color:var(--color-text-muted); cursor:pointer;">✕</button>
    `;

    container.appendChild(toast);

    setTimeout(() => {
      if (toast.parentElement) toast.remove();
    }, 3500);
  };

  // 7. Global Keyboard Shortcuts
  function initKeyboardShortcuts() {
    document.addEventListener('keydown', function (e) {
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

  // Initialize on DOM load
  document.addEventListener('DOMContentLoaded', function () {
    initDropdown();
    initMobileDrawer();
    initKeyboardShortcuts();

    // Restore saved store selection if present
    try {
      const savedStore = localStorage.getItem('retailsync-active-store');
      const storeSelect = document.getElementById('activeStoreSelect');
      if (savedStore && storeSelect) {
        storeSelect.value = savedStore;
      }
    } catch (e) {}

    // Restore saved role selection if present
    try {
      const savedRole = localStorage.getItem('retailsync-active-role');
      const roleSelect = document.getElementById('roleSwitcherSelect');
      if (savedRole && roleSelect) {
        roleSelect.value = savedRole;
      }
    } catch (e) {}
  });
})();
