# Maritime-CRM Task: Full Auth + Dashboard Optimization + Kanban DnD

## Plan Status: APPROVED ✅

**Completed Steps:**
- [x] 1. Create TODO.md
- [x] 2. Backend: Add user_id to models (SailorCreate/Update, VacancyCreate/Update, etc.) + auto-set from current_user
- [x] 3. Backend: Filter ALL list endpoints by user_id (get_sailors, get_vacancies, get_pipeline, etc.)
- [x] 4. Backend: Create /api/dashboard/summary (single aggregation pipeline, user-filtered stats/stages/expiring)
- [x] 5. Backend: Add MongoDB indexes (user_id, status, dates, stage) + /api/indexes endpoint
- [x] 6. Backend: Pipeline model +order:int + reorder endpoint
- [ ] 7. Backend: Update /api/seed to set user_id (admin demo)
- [x] 8. Frontend: cd frontend && npm i @dnd-kit/core @dnd-kit/sortable @dnd-kit/utilities
- [x] 9. Frontend: Add register form to LoginPage.js (POST /api/auth/register)
- [x] 10. Frontend: api.js - add getDashboardSummary(), updatePipelineOrder()
- [x] 11. Frontend: DashboardPage.js - switch to single summary API + memoization
- [ ] 12. Frontend: PipelinePage.js - @dnd-kit DnD (DndContext, columns SortableContext, cards draggable)
- [ ] 13. Test: Register user, verify data isolation, dashboard fast, DnD works
- [ ] 14. Demo: ?demo=1 bypass filter + seed works

**Next Step:** Frontend: PipelinePage.js DnD implementation (step 12)

**Instructions:** Call POST /api/indexes after login to create indexes. npm i @dnd-kit deps next.

**Instructions:** Update this file after each step completion.

