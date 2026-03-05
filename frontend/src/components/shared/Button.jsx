const Button = ({ onClick, label }) => (
  <button onClick={onClick} className="button">
    {label}
  </button>
);

export default Button;
