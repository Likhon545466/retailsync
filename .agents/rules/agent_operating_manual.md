# Universal Agent Operating Manual & Engineering Standards

This document establishes the universal operating protocol for AI coding agents. Any agent working on this or derived codebases must adhere to these foundational pillars.

---

## 0. Mandatory Pre-Execution Implementation Plan ("Plan Before Mutation")
- **Strict Non-Negotiable Rule:** Before applying ANY edits, mutating files, creating new modules, or going live with changes—**no matter how small or trivial the change is (even a 1-line typo fix, single CSS variable tweak, or simple config edit)**—the agent MUST FIRST communicate a structured **Implementation Plan** to the user.
- **Required Plan Structure:**
  1. **Objective & Targeted Files:** Explicit list of files and components to be modified.
  2. **Step-by-Step Technical Changes:** Specific description of code additions, modifications, or deletions.
  3. **Verification & Audit Strategy:** Exact commands, tests, or scripts that will validate the changes.
  4. **Risk & Invariant Safeguards:** Confirmation that existing test suites, database invariants, and UI tokens will not regress.
- **Workflow Protocol:** Present the plan clearly before making live changes.

---

## 1. Grounding & Investigation First ("Look Before You Leap")
- **Inspect Before Mutating:** Never assume the presence of libraries, module architectures, or API shapes. Inspect existing imports, package manifests (`package.json`, `pyproject.toml`, `requirements.txt`), and configuration files before writing code.
- **Trace Calling Sites:** Before changing a function signature or return type, search the entire codebase for all references and callers to prevent silent downstream regressions.
- **Verify Version Changes:** If using an API or framework that undergoes frequent breaking updates (e.g., Pydantic, LangChain, Next.js, Tailwind), check local versions or consult current documentation instead of guessing.

---

## 2. Minimal Invasive Surgery & Scope Control
- **Surgical Edits:** Make the minimal required change to satisfy the specification. Do not rewrite surrounding functions or overhaul entire files when a 5-line diff solves the problem.
- **Style & Convention Conformity:** Adopt the established naming conventions (camelCase, snake_case, PascalCase), indentation, and architectural design patterns already present in the repository.
- **Comment & Docstring Preservation:** Never delete, strip, or truncate existing comments, type annotations, or docstrings unless they are directly invalidated by the requested change.
- **Zero Unsolicited Refactoring:** Do not refactor untouched files, reformat unrelated modules, or reorganize directories unless explicitly directed by the user.

---

## 3. Mandatory Verification & Evidence-Based Delivery
- **Non-Negotiable Execution Loop:** Never report a task as complete without executing verification. "It looks correct in code" is not acceptable.
- **Three-Tier Verification Ladder:**
  1. *Syntax & Static Analysis:* Run linters and type checkers (`mypy`, `tsc`, `flake8`, `eslint`).
  2. *Automated Testing:* Execute existing unit, integration, or regression test suites.
  3. *Runtime Validation:* Execute the script, CLI command, or server endpoint to observe real output.
- **Transparent Evidence:** Include command outputs, test run summaries, or generated artifact verification directly in completion reports.

---

## 4. Root-Cause Debugging Protocol
- **No "Shotgun" Tweaking:** If an error or test failure occurs, do NOT start blindly changing parameters across multiple files.
- **Systematic Diagnosis:**
  1. Read the entire traceback and error output from top to bottom.
  2. Formulate a clear hypothesis explaining why the error occurred.
  3. Test the hypothesis with targeted logging or isolated inspection.
  4. Fix the exact root cause and verify that the error no longer reproduces.

---

## 5. Memory Externalization & Context Continuity
- **Single Source of Truth:** Keep persistent project state, architectural decisions, and current progress documented in living markdown files (`TODO.md`, `ROADMAP.md`, or `.agents/rules/`).
- **Resilience to Context Resets:** Treat each interaction turn as potentially losing working memory. Record:
  - Critical environment quirks (e.g., non-standard Python paths, special environment variables).
  - Key architectural decisions and why alternative approaches were rejected.
  - Remaining open tasks with clear blockers.

---

## 6. Workspace Discipline & Cleanliness
- **Zero Root Clutter:** Strictly enforce repository root hygiene. Never dump loose scratch scripts, temporary exports, raw outputs, or test files in the root folder.
- **Dedicated Subfolder Placement:** Place all deliverables, technical documentation, scripts, and legacy material in their dedicated subdirectories.
- **Scratch Lifecycle:** Use designated scratch directories (`scratch/` or `.scratch/`) for intermediate testing, and remove temporary artifacts upon task completion.

---

## 7. Safety, Idempotency & Blast-Radius Management
- **Destructive Action Protection:** Never run destructive or irreversible commands (`rm -rf`, `git reset --hard`, database drops, table truncations) without explicit user confirmation.
- **Idempotent Operations:** Design scripts and migrations so they can be executed multiple times safely without producing duplicate rows, corrupting files, or throwing unexpected errors.
- **Backup Before Massive Changes:** When performing large transformations across multiple files, ensure recent git commits exist or create an archive checkpoint before proceeding.

---

## 8. Clarification & Assumption Transparency
- **Surface Ambiguities Early:** If user instructions are ambiguous or allow two mutually exclusive architectures, present the options clearly with trade-offs rather than silently guessing.
- **State Working Assumptions:** When reasonable defaults must be chosen to maintain momentum, explicitly state what assumptions were made and where they can be configured or customized.
