# createContext() & useContext()
```createContext()``` and ```useContext()``` work together to let **deeply nested React components access shared data** without passing props through every level of the component tree.
<br/><br/>

To use ```createContext()``` &  ```useContext()``` in your React applications, start with importing both from React library.
```javascript
import { createContext, useContext } from 'react';
```

## How it works?
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
