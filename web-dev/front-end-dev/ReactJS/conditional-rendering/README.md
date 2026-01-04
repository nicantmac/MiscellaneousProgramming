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

<br/>

## Conditional rendering with ```if blocks```  (alternative from Ternanry render)
### Conditional renders using ```if blocks```
#### Syntax/ Example
```javascript
if (isLoading) {
  return <Spinner />;
}

if (error) {
  return <Error />;
}

return <Dashboard />;
```
so when there is multiple conditions or early exits and sometimes cleaner logic, these types of renders you'll see a lot more

<br/>

### Look out for logic errors
1. Conditioanl renders
- **```Reminder```**: when you want to render a component **ONLY** if a condition is true, and nothing if it is false.
```jsx
{isLoggedIn && <UserDashboard />}
// Use code with caution!
```
**Be careful with numbers!** <br/> 
- If the condition is 0, React will render 0 in the UI. <br/>
- Fix: Use a boolean check: ```{items.length > 0 && <List />}``` or ```{!!count && <Component />}```
