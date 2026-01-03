# useNavigate📍 
`useNavigate` is a React Router hook that allows you to **programmatically navigate** between routes in your application. 

<br/>

To use ```useNavigate()``` in your React applications, start with importing ```{ useNavigate }``` from React Router library.
```javascript
import { useNavigate } from 'react-router-dom';
```

<br/>

## How it works?
```javascript
export default function Home() {
  const navigate = useNavigate(); // Initialize the navigate function

  const handleClick() => {
    // Navigate to the '/dashboard' route when called
    navigate('/dashboard');
  };

  return (
    <div>
      <h1>Home Page</h1>
      <button onClick={handleClick}>Go to Dashboard</button>
    </div>
  );
}
```

<br/>

## Syntax Breakdown
```const navigate = useNavigate()```: returns a function (conventionally named navigate) that allows you to change the application's route imperatively, rather than using a declarative component like <Link>.

```navigate('/dashboard');```: the navigate function is then called with the desired path, typically within an event handler. 

```onClick={handleClick}```: function runs navigation path.

It’s commonly used after events like -> **form submissions, button clicks, or authentication actions.**

## When Should You Use ```useNavigate```?
- Clicking a button to change page
- Redirect after login
- Conditional navigation
