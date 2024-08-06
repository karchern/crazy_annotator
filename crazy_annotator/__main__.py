from crazy_annotator import objects
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    annotator = objects.annotator()
    print("Reading HMMs")
    annotator.read_hmms(path_to_hmm_file="/g/scb2/zeller/karcher/CAZY_project_v2/scripts/absolute_paths_all_cv_hmms_scratch.txt") # Good idea to move HMMs to scratch for faster input
    print("Reading sequences")
    annotator.read_sequences(path_to_sequences="/g/scb/zeller/karcher/kyanna_cazy_annotations/scripts/../results/prokka/086_scaffolds.faa")
    print("Annotating sequences (can take a few minutes; be patient)")
    annotator.annotate_sequences_with_all_hmms(threads = 16)
    print("Filtering and merging annotations over folds")
    annotator.curate_annotations(precomputed_hmm_cutoffs = "/g/scb2/zeller/karcher/CAZY_project_v2/results/CV_HMMs_optimal_cutoffs_all_v3.csv")
    breakpoint()
    annotator.annotations_filtered.to_csv("cazy_annotations.csv")
