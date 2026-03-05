const PromptDetail = ({ prompt }) => (
  <div className="prompt-detail">
    <h1>{prompt.title}</h1>
    <p>{prompt.description}</p>
    {/* Additional details and actions */}
  </div>
);

export default PromptDetail;
