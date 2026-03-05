const CollectionForm = ({ onSubmit }) => (
  <form className="collection-form" onSubmit={onSubmit}>
    <input type="text" name="name" placeholder="Collection Name" required />
    <button type="submit">Create Collection</button>
  </form>
);

export default CollectionForm;
