# 🧠 **Cursor AI Cheat Sheet for Big Projects**

---

### 🔍 1. **Ask Your Codebase Anything**
> Open AI Command Bar: `Cmd+K` (Mac) / `Ctrl+K` (Win/Linux)

**Examples:**
- `What does this function do?`
- `Where is this class used?`
- `Explain how authentication works in this project`
- `Which API endpoints modify user data?`

---

### ✍️ 2. **Edit with AI (Refactor/Rewrite)**
> Highlight code → Right-click → “Edit with AI”

**Prompts to Try:**
- `Refactor this to improve readability`
- `Convert to async/await`
- `Add error handling`
- `Split into smaller functions`
- `Rewrite using dependency injection`

---

### 🧪 3. **Generate or Improve Tests**
> In a test file or next to a function:

**Prompts:**
- `Write pytest unit tests for this`
- `Mock the external API in tests`
- `Add integration test coverage`

---

### 💬 4. **Use Smart Chat for Deep Questions**
> Right-click any file → “Ask AI”

**Ask:**
- `Explain this file in plain English`
- `Summarize this service`
- `How does this function interact with the database?`

---

### 🗂 5. **Work Across Multiple Files**
> In AI prompt, use:
```plaintext
In context:
- user/models.py
- user/services.py
```
**Then Prompt:**
`Refactor user creation to use transaction.atomic`

---

### ⚙️ 6. **Choose the Right Model**
> Bottom-right corner of Cursor window

- **GPT-4 Turbo** – Best for deep logic, refactoring, code gen.
- **Claude Opus** – Best for **long files** and large codebases.

---

### 🛠 7. **Handle TODOs With AI**
Add comments like:
```python
# TODO: clean up this logic
```
Then: "Edit with AI" → `Refactor for clarity and error handling`

---

### 🧭 8. **Navigate Like a Pro**
- `Cmd+P`: Fuzzy find any file
- `Cmd+Shift+F`: Search across project
- `Cmd+K`: Chat or run AI commands
- `Right-click`: Contextual AI options (Chat, Edit, Explain)

---

### 🖥 9. **Terminal & Git Integration**
- Run code/tests directly in the built-in terminal.
- Prompt AI with:
  - `Summarize recent changes`
  - `Write a commit message for these diffs`
  - `Review this PR for potential bugs`

---

### 🧑‍💻 10. **Pair Program With Cursor**
Ask high-level things like:
- `Design a plugin system for this Django app`
- `Help me architect a scalable auth system`
- `What are some risks in this implementation?`

