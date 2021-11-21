A = zeros(21);
for row = 1:21
    for col = (row + 1):(row + 6)
        if row == 21
                A(row,21) = 1;
        elseif mod(row - 1, col - row) == 0 
            if col < 21
                A(row,col) = 1/6;
            else
                A(row,21) = A(row,21) + 1/6;
            end
        else
            sub = 2*row - col;
            if sub > 0
                A(row,sub) = 1/6;
            else
                A(row,1) = A(row,1) + 1/6;
            end
        end
    end
end

Q = zeros(20);
for row = 1:20
    for col = 1:20
        Q(row,col) = A(row,col);
    end
end
N = inv(eye(20) - Q);
sum = 0;
for col = 1:20
    sum = sum + N(1,col);
end
format long
sum

format rat
k = 50; % can switch to 50 and 200
Achange = A^k;
prob = Achange(1,21)

while prob < 0.9
    k = k + 1;
    Achange = A^k;
    prob = Achange(1,21);
end

save('matrix.txt', 'A', '-ascii')