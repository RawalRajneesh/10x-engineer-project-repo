const PromptForm = ({ onSubmit }) => (
  <form className="prompt-form" onSubmit={onSubmit}>
    <input type="text" name="title" placeholder="Title" required />
    <textarea name="description" placeholder="Description" required></textarea>
    <button type="submit">Submit</button>
  </form>
);

export default PromptForm;
