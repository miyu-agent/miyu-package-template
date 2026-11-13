---
name: meeting-notes
description: "Keep meeting notes in notes/YYYY-MM-DD.md with decisions, owners and open questions. Use when the user asks to take or tidy meeting notes, 记笔记, 会议纪要."
metadata:
  display_name: Meeting notes
  summary: Meeting notes in a fixed format
  display_name_zh: 会议笔记
  summary_zh: 照固定格式记会议笔记
---

# Meeting notes

1. Create `notes/` in the workspace if it doesn't exist.
2. Write to `notes/YYYY-MM-DD.md` with today's date. If the file exists, append a new `## HH:MM` section instead of overwriting.
3. Use these sections, in this order, and leave out the empty ones:
   - `### Decisions`: one line each, what was decided.
   - `### Action items`: `- [ ] owner: task (due date)`.
   - `### Open questions`: what still needs an answer, and who should answer it.
4. Keep the user's own wording for names and terms. Don't invent owners or dates: ask if they are missing.
5. When done, tell the user the file path and how many action items there are.
