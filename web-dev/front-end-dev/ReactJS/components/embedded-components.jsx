// child component: this child destructures 'username' & 'comment' from the props object
function ReviewCard({ username, comment }) {
  return (
    <div className="p-4 border rounded-lg bg-white shadow-sm">
      <span className="font-bold text-blue-600">@{username}</span> {/* renders username */}
      <p className="text-gray-700 italic">"{comment}"</p> {/* renders comment */}
    </div>
  );
}

// parent component: the parent is responsible for data and layout
export default function ReviewSection() {
  // array of review objects
  const reviews = [
    { id: 1, user: "DevUser", text: "The 2025 React hooks are amazing!" },
    { id: 2, user: "Coder123", text: "Great component structure." }
  ];

  return (
    <section className="max-w-2xl mx-auto p-6 bg-gray-50 rounded-2xl">
      <h2 className="text-2xl font-bold mb-6">User Reviews</h2> {/* header */}

      <div className="space-y-4">
        {/* our .map() loops through reviews array to generate a list */}
        {reviews.map((rev) => (
          // reminder: 'key' is required by React to track list items
          <ReviewCard key={rev.id} username={rev.user} comment={rev.text} />
        ))}
      </div>

      {/* the footer displays the count of the reviews array */}
      <footer className="mt-8 pt-4 border-t text-center text-sm text-gray-400">
        Showing {reviews.length} verified reviews
      </footer>
    </section>
  );
}
