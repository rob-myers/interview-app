import { useQuery } from '@tanstack/react-query';

export default function CoramDemoApp() {

  // ✅ websocket
  // handling large number of results
  // - fixed size pages
  // - infinite scroll: only have a window, IntersectionObserver
  //   - ...
  // - lazy loaded of components in list

  const [websocketId, setWebsocketId] = React.useState(/** @type {undefined | number} */ (undefined));

  useQuery({
    queryKey: 'websocket-search',
    async queryFn() {
      // bootstrap websocket, using websocketId
      // onmessage from server, send data to SearchQueryComponent
      // use e.g. rxjs to put a delay between each incoming data item
      // React.context to communicate with SearchQueryComponent

    },
    retry: false,
    enabled: [typeof websocketId === 'number'],
    // ..
  });

  return (
    <div>
      <SearchQueryComponent />
      <div>
        <ResultsComponent />
      </div>
    </div>
  );

}

function SearchQueryComponent() {

  React.useContext(context)

  onSubmit

  return (
    <div>
      <input type="text" />
      <button type="button" onClick={onSubmit} />
      <div className="search-controls">
        {/* ... */}
      </div>
    </div>
  )
}

function ResultsComponent() {

  // results

  return (
    results.map(result =>
      <Result key={result.id} result={result} />
    )
  );
}
