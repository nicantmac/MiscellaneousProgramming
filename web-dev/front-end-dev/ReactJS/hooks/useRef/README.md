✅ useRef — What It Is & Why It Exists

useRef is a React Hook that lets you:

Store a value that does NOT cause re-renders

Directly access a DOM element

It’s basically React’s way of saying:

“I need to remember something, but I don’t want React to re-render.”

🔹 What useRef returns
const myRef = useRef(initialValue);


useRef() returns an object that looks like this:

{
  current: initialValue
}


You access the value with:

myRef.current

🧠 Key Difference From useState
useState	useRef
Triggers re-render	❌ Does NOT re-render
Used for UI data	Used for mutable values
Updates cause re-render	Updates are silent
Tracked by React	Stored between renders
---
🧠 When to use useRef

✅ DOM access (focus, scroll, measure size)
✅ Timers (setTimeout, setInterval)
✅ Tracking previous values
✅ Storing mutable data that shouldn’t trigger re-render

❌ When NOT to use useRef

❌ For rendering UI
❌ For values you want to display directly
❌ As a replacement for state

🧠 Mental Model (Very Important)

useState = “I want React to re-render when this changes”
useRef = “I just want to remember something”

const count = useRef(0);     // silent storage
const [num, setNum] = useState(0); // triggers re-render
