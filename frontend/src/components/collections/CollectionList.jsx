const CollectionList = ({ collections }) => (
  <div className="collection-list">
    {collections.map(collection => (
      <div key={collection.id}>{collection.name}</div>
    ))}
  </div>
);

export default CollectionList;
