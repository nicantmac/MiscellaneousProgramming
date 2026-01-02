/* - createContext: create a new Context object that can be used to pass data through the component tree without prop drilling
   - useContext: this consumes the value(s) provided by the nearest Context.Provider above it in the component tree
   - useState: allows you to add React state to functional components, often used with createContext to manage dynamic, global data  */ 
import React, { createContext, useContext, useState } from 'react';

/* createContext() is a function provided by React that creates two things: a Provider component 
   and a Consumer component however (the Consumer is less common now with the introduction of useContext)  */
const UserContext = createContext(); // 1. Create the Context via createContext()

// Grand-parent component: component creates & provides data for children components
export default function App() {
  // set data: user stores string, setUser changes and stores to user
  const [user, setUser] = useState("Guest");

  return (
    // 2. Wrap the parent with the Provider and pass the state data
    /* - utilize the .Provider on 'UserContext', now we can provide data to children (via DOM Tree) 
       - in 'value' should be the data you want available to all components nested within that provider */
    <UserContext.Provider value={{ user, setUser }}>
      <div style={{ padding: '20px', border: '1px solid black' }}>
        <h1>Grand-parent Component (App)</h1>
        <p>Current User: {user}</p>
        <hr />
        {/* The child can access the context because it’s rendered inside the parent */}
        <ProfilePage /> 
      </div>
    </UserContext.Provider>
  );
}

function ProfilePage() {
  return (
    <div>
      <h2>Parent Component (ProfilePage)</h2>
      <p>I don't use the data, but I pass it down automatically!</p>
      <UserButton /> {/* grandchild rendered here now has access to context data */}
    </div>
  );
}

function UserButton() {
  /* - user, setUser: with curly bracks we destructure and return data
     - useContext(UserContext): with passing provider 'UserContext', useContext looks up the component tree 
       and finds the nearest <UserContext.Provider>  */
  const { user, setUser } = useContext(UserContext); // grand-child can consume the context directly

  return (
    <div style={{ border: '1px solid blue', padding: '10px' }}>
      <h3>Child (UserButton)</h3>
      <p>Hello {user}</p>
      <button onClick={() => setUser("Jane Doe")}>
        Log In as Jane
      </button>
    </div>
  );
}
