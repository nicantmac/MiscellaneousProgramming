# useEffect
```useEffect``` is a fundamental React Hook that allows you to perform certain actions in function components after initial render from browser

<br/>To use `useEffect()` in your React applications, **start with** importing useEffect from React library.
```javascript
import { useEffect } from 'react';
```
<br/>

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
-→ [dependencies]: dependency array controls when the useEffect runs <br/><br/>

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
| Single [value]	When value changes | Runs on mount and when that specific value changes |
| With values [prop, state] | Runs on mount and only when one of those specific values change |

<br/>The Cleanup Function (Optional)
If your effect returns a function, React will run that function before the component unmounts or before the effect re-runs again. This is crucial for preventing memory leaks (i.e. clearing a timer or unsubscribing from a service).

```javascript
useEffect(() => {
  const timer = setInterval(() => console.log('Tick'), 1000);

  // Cleanup function
  return () => clearInterval(timer);
}, []);
```

## When to Use useEffect? (side effects actions, not rendering logic)

### Use it for:<br/>
```Fetching data```: It allows you to trigger an asynchronous API call after the component mounts so that the initial UI can render without waiting for data. For complex apps, developers often use libraries like TanStack Query which handle this logic internally.

```Timers / intervals```: You use it to start a setTimeout or setInterval when a component appears and, crucially, clear it using a cleanup function when the component disappears to prevent memory leaks.

```Event listeners```: It is used to attach listeners to the browser (e.g., window.addEventListener('resize', ...)) that React doesn't manage natively, ensuring they are removed when no longer needed.

```Syncing with external systems```: This is the primary "escape hatch" purpose—for example, initializing a non-React library (like a Google Map or jQuery widget) or maintaining a connection to a WebSocket. 

### Do not use it for:<br/>
```Simple derived state```: If you need a value that can be calculated from existing props or state (e.g., fullName = firstName + ' ' + lastName), calculate it directly in the component body. Using useEffect here creates an unnecessary second render.

```Basic calculations```: Standard logic should happen during the "render" phase. If a calculation is extremely expensive, use useMemo instead to cache the result.

```Rendering logic```: Any code that determines what the UI looks like should be "pure" and live directly in the component's main body, not inside an effect that fires after the UI is already painted. 

**if something can be derived directly from props or state — don’t put it in an effect.**
