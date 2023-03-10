#[macro_use]
extern crate matrix;

use matrix::prelude::*;

let mut sparse = Compressed::zero((2, 4));
sparse.set((0, 0), 42.0);
sparse.set((1, 3), 69.0);e

let dense = Conventional::from(&sparse);
assert!(
    &*dense == &*matrix![
        42.0, 0.0, 0.0,  0.0;
         0.0, 0.0, 0.0, 69.0;
    ]
);