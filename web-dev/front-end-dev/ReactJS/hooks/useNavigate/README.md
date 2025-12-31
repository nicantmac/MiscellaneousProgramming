# 📍 useNavigate – React Router Hook

`useNavigate` is a React Router hook that allows you to **programmatically navigate** between routes in your application. It’s commonly used after events like form submissions, button clicks, or authentication actions.

---

## 📦 Importing `useNavigate`

```js
import { useNavigate } from "react-router-dom";

🧠 When Should You Use useNavigate?
Situation	Use
Clicking a button to change page	✅ useNavigate
Redirect after login	✅ useNavigate
Conditional navigation	✅ useNavigate
Simple link in UI	❌ Use <Link> instead
