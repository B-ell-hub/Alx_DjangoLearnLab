## Posts & Comments API

### Posts Endpoints
- GET /api/posts/
- POST /api/posts/
- PUT /api/posts/{id}/
- DELETE /api/posts/{id}/
- Search: /api/posts/?search=keyword

### Comments Endpoints
- GET /api/comments/
- POST /api/comments/
- PUT /api/comments/{id}/
- DELETE /api/comments/{id}/

Authentication: Token-based
### Follow/Unfollow Users
- POST `/api/accounts/follow/<user_id>/` – Follow a user
- POST `/api/accounts/unfollow/<user_id>/` – Unfollow a user

### Feed Endpoint
- GET `/api/feed/` – Shows posts from users you follow, ordered by most recent
