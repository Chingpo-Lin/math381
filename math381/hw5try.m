 x = [1;1;1];
 y = [2;2;2]; 
 u = [1 2 3];
 v = [4 5 6];
 
 dot(x,y);
 dot(x,u);
 dot(y,x);
 dot(u,x);
 A = randn(3);
 eig(A);
 
 x = [-1 2 1];
 x > 0;
 
 A = randn(20);
 x = randn(20,1);
 y = randn(20,1);
 z = randn(1,20);
 x.*y