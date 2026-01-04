# useRef
```useRef``` is a React Hook that lets you store a value that **does NOT** cause re-renders
<br/>
To use useRef() in your React applications, start with importing ```useRef``` from React library.
```javascript
import { useRef } from 'react';
```

## How it works?
```javascript
import { useRef } from 'react';

export default function Counter() {
  let ref = useRef(0);  /* sets a ref object whose current property is set to 0 */

  function handleClick() {
    ref.current = ref.current + 1;
    alert('You clicked ' + ref.current + ' times!');
  }

  return (
    <button onClick={handleClick}>
      Click me!
    </button>
  );
}
```
## Syntax breakdown
```let ref = useRef(0);```: useRef(0) in React creates a plain object like ```{ current: initialValue }```, and ```.current``` accesses that data.<br/><br/>
```ref.current = ref.current + 1;```: access the value & adds 1 to the current value and stores that update into current<br/><br/>
```onClick={handleClick}```: function runs useRef logic<br/>

It’s basically React’s way of saying: “I need to remember something, but I don’t want React to re-render.”

## When to utilize useRef?
| ✔️ When to use | ❌ When NOT to use useRef |
|----|----|
| DOM access (focus, scroll, measure size) | For rendering UI |
| Timers (setTimeout, setInterval) | For values you want to display directly|
| Tracking previous values |  As a replacement for state |
| Storing mutable data that shouldn’t trigger re-render |

<br/>

## Key Difference From useState
#### 🔹 Mental Model (Very Important)
```useState``` -→ “I want React to re-render when this changes”
```javascript
const [num, setNum] = useState(0); // triggers re-render
```
```useRef``` -→ “I just want to remember something”
```javascript
const count = useRef(0); // silent storage
```

| useState | useRef |
|----|----|
| Triggers re-render | Does NOT re-render |
| Used for UI data | Used for mutable values |
| Updates cause re-render |	Updates are silent |
| Tracked by React | Stored between renders |
