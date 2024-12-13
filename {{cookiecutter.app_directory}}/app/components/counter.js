import Alpine from "alpinejs";

function Counter()
{
    return {
        count: 0,
    };
}

Alpine.data("counter", Counter);

export default Counter;
