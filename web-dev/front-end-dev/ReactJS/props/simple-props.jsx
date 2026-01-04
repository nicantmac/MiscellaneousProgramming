// Child component
function WelcomeMessage(props) {
   /* writing "props" now holds all data stated from parent.
      use dot notation to access values, i.e. props.name -> Jordan */
  return (
    <div style={{ border: "1px solid #ccc", padding: "10px" }}>
      {/* dot notation let's us access specific data */}
      <h1>Hello, {props.name}!</h1>
      <p>You have {props.messageCount} new notifications.</p>
    </div>
  );
}

// Parent component
export default function App() {
  return (
    <div>
      {/* created child component to show user name & message count */}
      <WelcomeMessage name="Jordan" messageCount={5} />
      <WelcomeMessage name="Taylor" messageCount={0} />
    </div>
  );
}
