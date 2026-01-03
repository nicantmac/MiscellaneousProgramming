# useEffect
```useEffect``` is a fundamental React Hook that allows you to perform certain actions in function components after initial render from browser

<br/>To use `useEffect()` in your React applications, **start with** importing useEffect from React library.
```javascript
import { useEffect } from 'react';
```

## How it works?
```javascript
export default function App() {
   useEffect(() => {
     // side effect logic
   }, [dependencies]);
}
```
**```useEffect()```** re-renders it returns a two-element array: (state) & (function) respectively <br/>
-→ curly bracks{}: stores code that React runs after component renders or when your specific dependencies change <br/>
-→ [dependencies]: dependency array controls when the useEffect runs <br/>

## What is useEffect for?
reminder: useEffect runs after a component renders or dependency changes. It lets your component react to changes in state, props, or lifecycle events.<br/>

<br/>**Inside the curly brackets, it's typical to:**
- Data Fetching: Requesting data from an API.
- Manual DOM Manipulation: Changing document titles or focusing elements.
- Subscriptions: Setting up WebSockets or event listeners.
- Timers: Initializing setTimeout or setInterval

<br/>**Inside the dependency array, it's typical to:**
| Dependency Array | Behavior |
| ------------- | ------------- |
| No array | Runs after every render |
| Empty array [] | Runs only once after the initial mount (component appears) |
| With values [prop, state] | Runs on mount and only when those specific values change |

The Cleanup Function (Optional)
If your effect returns a function, React will run that function before the component unmounts or before the effect re-runs again. This is crucial for preventing memory leaks (i.e. clearing a timer or unsubscribing from a service).

```javascript
useEffect(() => {
  const timer = setInterval(() => console.log('Tick'), 1000);

  // Cleanup function
  return () => clearInterval(timer);
}, []);
```


---
🧠 Key Concepts
Concept	Meaning
Dependency Array	Controls when effect runs
Cleanup Function	Runs before unmount or re-run
Empty Array []	Runs once
No Array	Runs every render
---
✅ When to Use useEffect

Use it for:

Fetching data

Timers / intervals

Event listeners

Syncing with external systems

Do not use it for:

Simple derived state

Basic calculations

Rendering logic

---
useEffect is for side effects, not rendering logic.

If something can be derived directly from props or state — don’t put it in an effect.

---
🔍 Summary Table
Dependency Array	Runs When
None	Every render
[]	Once (on mount)
[value]	When value changes
[a, b]	When a or b changes
---
🧠 Mental Model (Memorize This)

useEffect runs after render,
and reruns when anything in the dependency array changes.
---
