# useState 
`useState` a fundamental React Hook that lets functional components manage and store data **(state)** that can change over time.
 When updated, this triggers a re-render, which is crucial for dynamic UIs like counters or form inputs

To use `useState()` in your React applications, **start with** importing useState from React library.
```bash
import { useState } from 'react';
```

## How it works?
```
export default function App() {
  const [state, setState] = useState(initialValue);  ←-
  // ...
}
```
```useState``` returns it returns a two-element array: (state) & (function) respectively
state: stores the current state/data, setState: a function to update state/data


## Files
- `BasicCounter.jsx` – numeric state updates
- `ToggleBoolean.jsx` – boolean toggling
- `InputControlled.jsx` – controlled form inputs

These examples focus on understanding state updates, not app structure.
