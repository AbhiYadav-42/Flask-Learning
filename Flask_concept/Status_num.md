# 📘 HTTP Status Codes Cheat Sheet

---

## ✅ 2xx – Success
| Code | Meaning          | When to Use |
|------|------------------|-------------|
| 200  | OK               | Standard success response (e.g., returning data or a webpage). |
| 201  | Created          | A new resource was successfully created (e.g., user signup). |
| 202  | Accepted         | Request accepted but processing later (asynchronous tasks). |

---

## 🔄 3xx – Redirection
| Code | Meaning              | When to Use |
|------|----------------------|-------------|
| 301  | Moved Permanently    | Resource has a new permanent URL (SEO friendly redirect). |
| 302  | Found (Temporary)    | Redirecting temporarily (e.g., login → dashboard). |
| 304  | Not Modified         | Cached version is still valid (saves bandwidth). |

---

## ⚠️ 4xx – Client Errors
| Code | Meaning          | When to Use |
|------|------------------|-------------|
| 400  | Bad Request      | Invalid input sent by client (e.g., malformed JSON). |
| 401  | Unauthorized     | Authentication required (e.g., API call without token). |
| 403  | Forbidden        | Client authenticated but not allowed (e.g., normal user in admin panel). |
| 404  | Not Found        | Resource doesn’t exist (e.g., `/profile/123` not found). |
| 405  | Method Not Allowed | HTTP method not allowed (e.g., POST on a GET endpoint). |

---

## 💥 5xx – Server Errors
| Code | Meaning              | When to Use |
|------|----------------------|-------------|
| 500  | Internal Server Error| Generic error (e.g., server crash, code bug). |
| 502  | Bad Gateway          | Server acting as proxy got invalid response. |
| 503  | Service Unavailable  | Server overloaded or under maintenance. |
| 504  | Gateway Timeout      | Server took too long to respond. |

---

✅ Use this cheat sheet while building Flask apps to decide **which status code** to return in each situation.
