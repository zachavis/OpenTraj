import sys
from opentraj.toolkit.core.trajdataset import TrajDataset
from opentraj.toolkit.core.trajlet import split_trajectories


# TODO: to be added later
def grouping(dataset: TrajDataset):
    return


def run():
    opentraj_root = sys.argv[1]
    output_dir = sys.argv[2]

    datasets = get_datasets(opentraj_root, all_dataset_names)
    for ds in datasets:
        grouping(ds)


if __name__ == "__main__":
    from opentraj.toolkit.test.load_all import get_datasets, all_dataset_names
    run()



