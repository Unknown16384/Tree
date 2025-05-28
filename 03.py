def dfs(node, type='preorder'):
    if not node: return
    elif type == 'preorder':
        print(node.value, end=' ')
        dfs(node.left, 'preorder')
        dfs(node.right, 'preorder')
    elif type == 'inorder':
        dfs(node.left, 'inorder')
        print(node.value, end=' ')
        dfs(node.right, 'inorder')
    elif type == 'postorder':
        dfs(node.left, 'postorder')
        dfs(node.right, 'postorder')
        print(node.value, end=' ')
    else: return