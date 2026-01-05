# createContext() & useContext()
```createContext()``` and ```useContext()``` work together to let **deeply nested React components access shared data** without passing props through every level of the component tree.
<br/><br/>

To use ```createContext()``` &  ```useContext()``` in your React applications, start with importing both from React library.
```javascript
import { createContext, useContext } from 'react';
```

## How it works?
### Really Quick on why we utilize ```createContext``` & ```useContext```
We want to **avoid** this thing called **```Prop drilling```** is the process of passing data (props) down through multiple nested components in a React component tree, even when the intermediate components do not need the data themselves.<br/><br/>
The following example shows how data passes through: ```App → Parent → Child → Grandchild```<br/>
```jsx
function App() {
  const data = 'Hello from App';
  return <Parent data={data} />; // App passes 'data' to Parent
}

function Parent({ data }) {
  // Parent doesn't use 'data', but passes it to Child
  return <Child data={data} />;
}

function Child({ data }) {
  // Child doesn't use 'data', but passes it to Grandchild
  return <Grandchild data={data} />;
}

function Grandchild({ data }) {
  return <p>{data}</p>; // Grandchild finally uses 'data'
}
```
```Parent``` and ```Child``` components are part of the **prop drilling** process because they don't consume the data prop but must accept and pass it down the for it to get to ```Grandchild```. 

#### Drawbacks:
- Reduced Readability: It becomes harder to track the flow of data through many layers of components, making the codebase messy and difficult to understand.
- Tightly Coupled Components: Components become dependent on the specific structure of the component tree, making it difficult to refactor or reuse them in different parts of the application without modifications.
- Unnecessary Re-renders: When the prop changes, all intermediate components often re-render, even if they don't use the prop, which can lead to performance issues. 

Overall from Prop Drilling, we can solve this in many ways. The most common in React is Context API.
```React Context API```: A built-in React feature that allows data to be shared across the component tree without passing props manually at every level. This is ideal for managing global state like themes, user authentication status, or language preferences.

<br/>

### Syntax Breakdown
```javascript
import { createContext, useContext } from 'react';

// 1. Create the Context via createContext() 
const UserContext = createContext();

function App() {
  const [user, setUser] = useState('Guest');

  return (
    // All components within the Provider can access the data stored in 'user'
    <UserContext.Provider value={user}>
      <UserProfile />
    </UserContext.Provider>
  );
}

function UserProfile() {
  const { user, setUser } = useContext(UserContext); // destruct the data you want from provider component
  return (
    <div>
      <p>Hello {user}</p>
      <button onClick={() => setUser("Jane Doe")}>
         Log In as Jane
      </button>
    </div>
  );
}
```

<br/>

## What Is ```createContext()```?
```javascript
import { createContext } from "react";

const UserContext = createContext();
```
```createContext()``` creates a Context object, giving access to the properties .Provider and .Consumer
<br/><br/>
```Provider```: This is a React component (i.e. <MyContext.Provider>) used to wrap the part of the component tree that needs access to the shared data. It accepts a value prop, which is the data made available to all descendants.<br/>

```Consumer```: This is a legacy component (i.e. <MyContext.Consumer>) for accessing the context value. In modern functional components, the useContext hook is the preferred and more concise way to consume the context.<br/>

<br/>

## What Is ```useContext()```?
```javascript
import { useContext } from "react";

const { user, setUser} = useContext();
```
```useContext()``` is a React Hook that lets a component read data from a Context.<br/>
**It basically tells React:** “Give me the value from the nearest <UserContext.Provider> above me.”
Provider supplies the data

useContext() reads the data

user and setUser come from the provider’s value

Any component inside the provider can access it
