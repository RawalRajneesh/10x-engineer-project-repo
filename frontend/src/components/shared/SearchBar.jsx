const SearchBar = ({ onSearch }) => (
  <input
    type="search"
    placeholder="Search..."
    onChange={(e) => onSearch(e.target.value)}
    className="search-bar"
  />
);

export default SearchBar;
