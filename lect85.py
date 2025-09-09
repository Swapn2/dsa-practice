#  preorder / Inorder / postorder


class Node:
    def __init__(self, data , left = None , right = None):
        self.data = data 
        self.right = right 
        self.left = left 

root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)


def preinposttraversal(root):
    node = root
    pre = []
    In = []
    post = []
    if root == None:
        return 
    st=[]
    st.append((root,1))
    while(st):
        node,state = st.pop()
        if state ==1:
            pre.append(node.data)
            state = 2
            st.append((node,state))
            if node.left:
                st.append((node.left,1))
        elif state ==2:
            In.append(node.data)
            state = 3
            st.append((node,state))
            if node.right:
                st.append((node.right,1))
        else:
            post.append(node.data)
    print(pre)
    print(In)
    print(post)
    # return pre,In,post

print(preinposttraversal(root))