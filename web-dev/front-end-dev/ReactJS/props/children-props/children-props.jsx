// child component (helper)
function Card({ children }) {
  return (
    <div className="child-section">
      {children} {/* This is the slot where the Parent's h1 and p tags will go */}
    </div>
  );
}

// parent component
export default function App() {
  return (
    <Card>
      {/* Everything here becomes the "children" */}
      <h1>Welcome to my Page</h1>
      <p>This text is sitting inside the Card's shell.</p>
    </Card>
  );
}
