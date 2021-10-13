#include <memory>

#include "binary_tree_node.h"
#include "test_framework/binary_tree_utils.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::unique_ptr;
using namespace std;

pair<int, BinaryTreeNode<int> *> myLca(const unique_ptr<BinaryTreeNode<int>> &tree,
                                       const unique_ptr<BinaryTreeNode<int>> &node0,
                                       const unique_ptr<BinaryTreeNode<int>> &node1)
{

  if (tree == nullptr)
  {
    return make_pair(0, nullptr);
  }

  // int totalNodes = 0;
  int total=0;

  if (tree==node0){
    total++;
  }

  if (tree==node1){
    total++;
  }

  auto leftRes = myLca(tree->left, node0, node1);
  auto rightRes = myLca(tree->right, node0, node1);

  if (leftRes.second != nullptr){
    return make_pair(2,leftRes.second);
  }

  if (rightRes.second != nullptr){
    return make_pair(2,rightRes.second);
  }

  int totalAmt=total+leftRes.first+rightRes.first;

  if (totalAmt==2){
    return make_pair(totalAmt,tree.get());
  }


  return make_pair(totalAmt,nullptr);



}

BinaryTreeNode<int> *Lca(const unique_ptr<BinaryTreeNode<int>> &tree,
                         const unique_ptr<BinaryTreeNode<int>> &node0,
                         const unique_ptr<BinaryTreeNode<int>> &node1)
{
  // TODO - you fill in here.

  auto res=myLca(tree,node0,node1);

  return res.second;
}
int LcaWrapper(TimedExecutor &executor,
               const unique_ptr<BinaryTreeNode<int>> &tree, int key0,
               int key1)
{
  const unique_ptr<BinaryTreeNode<int>> &node0 = MustFindNode(tree, key0);
  const unique_ptr<BinaryTreeNode<int>> &node1 = MustFindNode(tree, key1);

  auto result = executor.Run([&]
                             { return Lca(tree, node0, node1); });

  if (!result)
  {
    throw TestFailure("Result can not be nullptr");
  }
  return result->data;
}

int main(int argc, char *argv[])
{
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "tree", "key0", "key1"};
  return GenericTestMain(args, "lowest_common_ancestor.cc",
                         "lowest_common_ancestor.tsv", &LcaWrapper,
                         DefaultComparator{}, param_names);
}
