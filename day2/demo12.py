def outer_fn():
    def inner_fn():
        print("--- inside inner_fn----")
    return inner_fn
    # print("--- inside outer fun----")

fn=outer_fn()
fn()