// You should keep helper components in the same file when:

// ✔ They are only used by that one component
// ✔ They exist purely to support the main component
// ✔ They are small (UI fragments, not full features)
// ✔ You don’t expect to reuse them elsewhere

// ui skeletons show filler animation for where will soon pop up 
function ItemSkeleton() {
  return <div className="p-4 border rounded animate-pulse">Loading...</div>;
}

// we mapped through 'items object' as item and passed it here
function ItemCard({ item }) {
  return (
    <div className="p-4 border rounded">
      <h3 className="font-bold">{item.title}</h3> {/* render the title value from the current item */}
      <p className="text-sm text-gray-600">{item.count} terms</p> {/* here we render the count value from the current item */}
    </div>
  );
}

// this is our parent component
export default function HomeMini() {

  // Data only flows down from HomeMini (the parent) to ItemCard (the child).
  // ItemCard cannot change the data; it can only display what it was given. 

  const isLoading = false;
  const items = [{ id: 1, title: "Biology", count: 12 }];

  return (
    <main className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">Your Library</h1>

      {/* conditional render: show Skeleton when loading to hint where
          data shows, render "no sets" if items is empty, or we display each ItemCard */}
      {isLoading ? (
        <ItemSkeleton />
      ) : items.length === 0 ? (
        <p>No sets yet.</p>
      ) : (
        <div className="grid gap-3">
          {items.map((item) => (
            <ItemCard key={item.id} item={item} />
          ))}
        </div>
      )}
    </main>
  );
}
