const Modal = ({ isOpen, onClose, children }) => (
  isOpen ? (
    <div className="modal">
      <div className="modal-content">
        <button onClick={onClose}>Close</button>
        {children}
      </div>
    </div>
  ) : null
);

export default Modal;
