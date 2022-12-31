// Your code here!
use proconio::input;

fn main(){
	input! {
      n:usize,
      k:usize,
      mut a:[u8;n],
  }
  for _ in 0..k {
    a.remove(0);
    a.push(0);
  }  
  a.iter().for_each(|v| print!("{} ",v));
}