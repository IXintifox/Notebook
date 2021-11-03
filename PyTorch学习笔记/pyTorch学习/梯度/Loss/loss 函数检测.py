import torch

target = torch.tensor([3,4,7,9])

for i in range(20000):
    x = torch.randn(4, 10)
    test = torch.argmax(x, dim=1)
    compare = torch.eq(test, target)

    if compare[0] == 0:
        continue
    else :
        break

print(test)
p = compare.sum()
print((p.float().item())/4)