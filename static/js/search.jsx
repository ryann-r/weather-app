// SEARCH

function Search() {
    const [searchInput, setSearchInput] = React.useState({ city: '' });

    const handleChange = (event) => {
        const value = event.target.value;
        setSearchInput({
            [event.target.name]: value
        });
        console.log("value", value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch('/api/search-input', {
            method: 'POST',
            body: JSON.stringify( searchInput ),
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
    }


    return (
        <form onSubmit={handleSubmit}>
            <label>
                Search City
                <input type="text"
                name="city"
                placeholder="Enter City"
                onChange={handleChange}
                value={searchInput.city} />
            </label>
            <input type="submit" value="Submit" disabled={!searchInput.city} />
        </form>
    )
}