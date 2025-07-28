# Q1: What are the differences between a class component and a functional component?

A functional component is a JavaScript function, whereas a Class component is an instance of a particular class i.e. React.ClassComponent (?). The former uses _hooks_ whereas the latter uses "lifecycle methods": mounting, updating, unmounting, error handling. The former returns a `React.Element` whereas the latter has a render function returning such a value.

# Q2: What are React Hooks? Name a few commonly used ones.

Hooks provide features to a functional components whilst keeping the function "pure" i.e. they do not mutate the underlying Object of the function.

They rely on the ordering in which they are executed to maintain state (e.g. in useRef and useState).
They also support hot-reloading (React fast-refresh).

Examples:

- React.useRef
- React.useState
- React.useMemo
- React.useEffect

# Q3: How does useEffect work, and how is it different from componentDidMount or componentDidUpdate?

`React.useEffect(callback, deps)`

On each React render, after the DOM mutations have been applied, the callback is executed if the deps have changed (or initially, or during hot-reload). If the callback returns a function (clean up),
that function is executed before re-executing the callback.

It covers both `componentDidMount` (via `[]`) and `componentDidUpdate`.
There are some differences e.g. hot reloading for `[]`.

# Q4: Explain reconciliation in React.

This is the underlying "diffing algorithm" i.e. how React decides to update the DOM.

It is based on (a) different "types" will induce different trees, (b) user-assigned props.key hint that this is the same component possibly across re-orderings.


# Q5: What is the Virtual DOM and why is it important?

The virtual DOM is React's internal representation of the actual DOM.
Its important for performance e.g. by diffing we can avoid unnecessary DOM mutations.


# Code Challenge: Build a simple counter using useState and useEffect.

```tsx

function SimpleCounter(props: Props) {
  const [count, setCount] = React.useState(0);

  // auto-count
  React.useEffect(() => {
    const intervalId = window.setInterval(() => {
      setState(x => x + 1);
    }, 1000);
    return () => window.clearInterval(intervalId);
  }, []);


  return (
    <div>
      <div>{count}</div>
      <button type="button" onClick={() => setState(x => x + 1)}>Increment</button>
    </div>
  )
}
```


# System Design Scenario: How would you build a Todo App in React with the following features:

- Add new todos
- Mark as complete
- Delete todos
- Persist in local storage
- Walk through:
- Folder structure
- State management choices (Context API, Redux, etc.)
- Component hierarchy
- Performance considerations

... 🚧