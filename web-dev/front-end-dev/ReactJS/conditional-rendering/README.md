# Various Rendering in React
Rendering -→ React basically deciding what JSX becomes visible on the screen

## Different types of rendering?
- Ternary rendering (most common)
- Conditional rendering (short-circut rendering)
- Conditional rendering with ```if``` (outside JSX)

React is constantly asking: “What should I show right now based on the current data?”

<br/>

## Most common type of render
### Ternary Render
#### Syntax
```javascript
condition ? renderIfTrue : renderIfFalse
```
#### Real-world example
```javascript
{isLoggedIn ? <Dashboard /> : <Login />}
```
so when user is logged in, let's show their dashboard, if not let's prompt user to login

So ultimately, whenever you want something between two clear states

<br/>

## Second most common type of render
### Conditional Render or (short-circut render)
#### Syntax
```javascript
condition && <Component />
```
#### Real-world example
```javascript
{isLoading && <Spinner />}
```
so **ONLY** when isLoading is ```true```, let's render loading animation component. If ```false``` nothing happens we move on

So ultimately, devs conditionally render when there is no need for an ```else block``` render


This guide covers the formal terms, patterns, and "gotchas" of conditional rendering in React, formatted for quick reference in projects or interview prep.
1. Logical AND (&&) Operator
Formal Term: Short-Circuit Evaluation.
Use Case: When you want to render a component ONLY if a condition is true, and nothing if it is false.
jsx
// The "Short-Circuit" Pattern
{isLoggedIn && <UserDashboard />}
Use code with caution.

Interview Tip: Be careful with numbers! If the condition is 0, React will render 0 in the UI.
Fix: Use a boolean check: {items.length > 0 && <List />} or {!!count && <Component />}.
2. Ternary Operator (condition ? true : false)
Formal Term: Inline Conditional Expression.
Use Case: When you need an "either-or" logic (If true, show A; if false, show B).
jsx
{isAdmin ? (
  <AdminPanel />
) : (
  <AccessDenied />
)}
Use code with caution.

3. Early Return (Guard Clauses)
Formal Term: Guard Pattern.
Use Case: Preventing a component from rendering anything at all based on a condition at the top of the function.
javascript
function Profile({ user }) {
  // If no user, "Guard" the rest of the component
  if (!user) {
    return null; // Or <LoadingSpinner />
  }

  return <div>Welcome, {user.name}</div>;
}
Use code with caution.

4. Element Variables
Formal Term: Variable Assignment Rendering.
Use Case: When logic is complex and would make the JSX return statement messy and hard to read.
javascript
let button;
if (isLoggedIn) {
  button = <LogoutButton onClick={handleLogout} />;
} else {
  button = <LoginButton onClick={handleLogin} />;
}

return (
  <nav>
    <Logo />
    {button}
  </nav>
);
Use code with caution.

5. Switch Statements or Object Literals
Formal Term: Mapping/Dispatcher Pattern.
Use Case: When you have many possible states (e.g., 'loading', 'error', 'success', 'empty').
javascript
const StatusMessage = ({ status }) => {
  const content = {
    loading: <Spinner />,
    error: <ErrorView />,
    success: <DataView />,
  };

  return <div>{content[status] || <DefaultView />}</div>;
};
Use code with caution.

6. React Suspense (Modern Approach)
Formal Term: Declarative Loading States.
Use Case: Automatically handling "waiting" states for data fetching or code splitting.
jsx
import { Suspense } from 'react';

<Suspense fallback={<Spinner />}>
  <SlowComponent />
</Suspense>
Use code with caution.

💡 Interview Summary Table
Term	Syntax	Best For
Short-Circuit	{condition && <Box />}	Simple "Show or Hide"
Ternary	{cond ? <A /> : <B />}	Either/Or logic
Early Return	if (!data) return null	Component-level protection
Suspense	<Suspense fallback={...}>	Async data/Lazy loading
Key Interview Keywords to Use:
Declarative UI: We describe what the UI should look like for a state, not how to change the DOM.
Truthy/Falsy: Understanding how JS evaluates non-boolean values in JSX.
Reconciliation: How React efficiently updates the DOM when these conditions change.
