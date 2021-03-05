function App() {

    return (
        <React.Fragment>
            <ReactRouterDOM.BrowserRouter>
                <ReactRouterDOM.Switch>
                    <ReactRouterDOM.Route path='/' exact>
                        <Home />
                    </ReactRouterDOM.Route>
                    <ReactRouterDOM.Route path='/weather-forecast'>
                        <DisplayWeather />
                    </ReactRouterDOM.Route>
                </ReactRouterDOM.Switch>
            </ReactRouterDOM.BrowserRouter>
        </React.Fragment>
    )

}

ReactDOM.render(
    <App />,
    document.getElementById('root')
);