#include <memory>

#include "bst_node.h"
#include "test_framework/binary_tree_utils.h"
#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::unique_ptr;

// Input nodes are nonempty and the key at s is less than or equal to that at
// b.

bool BothLesser(BstNode<int> *currSubTree, const unique_ptr<BstNode<int>> &s,
                 const unique_ptr<BstNode<int>> &b)
{

  bool result = currSubTree && currSubTree->data > s->data && currSubTree->data > b->data;
  return result;
}

bool BothGreater(BstNode<int> *currSubTree, const unique_ptr<BstNode<int>> &s,
                const unique_ptr<BstNode<int>> &b)
{
  bool result = currSubTree && currSubTree->data < s->data && currSubTree->data < b->data;
  return result;
}
BstNode<int> *FindLca(const unique_ptr<BstNode<int>> &tree,
                      const unique_ptr<BstNode<int>> &s,
                      const unique_ptr<BstNode<int>> &b)
{
  // TODO - you fill in here.

  auto currSubTree = tree.get();
  while (currSubTree && (BothLesser(currSubTree, s, b) || BothGreater(currSubTree, s, b)))
  {
    while (currSubTree && (BothLesser(currSubTree, s, b)))
    {
      currSubTree = currSubTree->left.get();
    }
    while (currSubTree && (BothGreater(currSubTree, s, b)))
    {
      currSubTree = currSubTree->right.get();
    }
  }

  return currSubTree;
}
int LcaWrapper(TimedExecutor &executor,
               const std::unique_ptr<BstNode<int>> &tree, int key0, int key1)
{
  const unique_ptr<BstNode<int>> &node0 = MustFindNode(tree, key0);
  const unique_ptr<BstNode<int>> &node1 = MustFindNode(tree, key1);

  auto result = executor.Run([&]
                             { return FindLca(tree, node0, node1); });

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
  return GenericTestMain(args, "lowest_common_ancestor_in_bst.cc",
                         "lowest_common_ancestor_in_bst.tsv", &LcaWrapper,
                         DefaultComparator{}, param_names);
}
