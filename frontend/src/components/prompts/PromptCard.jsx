const PromptCard = ({ prompt }) => (
  <div className="prompt-card">
    <h2>{prompt.title}</h2>
    <p>{prompt.description}</p>
    {/* Further display details */}
  </div>
);

export default PromptCard;
