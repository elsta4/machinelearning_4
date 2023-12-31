import numpy as np

def euclidean_distance(x, y):
    """
    :param x: D-dimensional vector
    :param y: D-dimensional vector
    :return: dist - scalar value
    """

    dist = 0 # TODO: implement 
    return dist


def objective_function(X, K, ind_samples_clusters, centroids):
    """
    :param X: data for clustering, shape: (N, D), with N - number of data points, D - dimension
    :param K: number of clusters
    :param ind_samples_clusters: indicator variables for all data points, shape: (N, K)
    :param centroids: means of clusters, K vectors of dimension D, shape: (K, D)
    :return: objective function J - a scalar value
    """

    J = 0
    N = X.shape[0]

    # TODO: implement
    return J


def closest_centroid(sample, centroids):
    """
    :param sample: a data point x_n (of dimension D)
    :param centroids: means of clusters, K vectors of dimension D, shape: (K, D)
    :return: idx_closest_cluster, that is, the index of the closest cluster
    """
    # Calculate distance of the current sample to each centroid
    # Return the index of the closest centroid (int value from 0 to (K-1))
    
    distances = [0] # TODO: change
    idx_closest_cluster = 0 # TODO: change

    return idx_closest_cluster


def assign_samples_to_clusters(X, K, centroids):
    """
    :param X: data for clustering, shape: (N, D), with N - number of data points, D - dimension
    :param K: number of clusters
    :param centroids: means of clusters, K vectors of dimension D, shape: (K, D)
    :return: ind_samples_clusters: indicator variables for all data points, shape: (N, K)
    """

    N = X.shape[0] # N - number of samples

    ind_samples_clusters = np.zeros((N, K))

    # TODO: implement
    # Here you will need to call the closest_centroid() function

    assert np.min(ind_samples_clusters) == 0 and np.max(ind_samples_clusters == 1), "These must be one-hot vectors"
    return ind_samples_clusters

def recompute_centroids(X, K, ind_samples_clusters):
    """
    :param X: data for clustering, shape: (N, D), with N - number of data points, D - dimension
    :param K: number of clusters
    :param ind_samples_clusters: indicator variables for all data points, shape: (N, K)
    :return: centroids - means of clusters, shape: (K, D)
    """

    D = X.shape[1]
    centroids = np.zeros((K, D))
    
    # TODO: Implement the equation

    return centroids

def kmeans(X, K, max_iter):
    """
    :param X: data for clustering, shape: (N, D), with N - number of data points, D - dimension
    :param K: number of clusters
    :param max_iter:
    :return: ind_samples_clusters - indicator variables for all data points, shape: (N, K)
            centroids - means of clusters, shape: (K, D)
            lst_J - an list with values of the objective function J over iteration
    """

    N, D = X.shape

    # Init centroids
    rnd_points = np.random.choice(np.arange(N), size=K, replace=False)  
    centroids = X[rnd_points, :]
    eps = 1e-6

    assert centroids.shape[0] == K and centroids.shape[1] == D
    print(f'Init centroids: {centroids}')

    lst_J = []
    for it in range(max_iter):    
        # Assign samples to the clusters
        ind_samples_clusters = None # TODO: function call to assign samples to clusters
        J = 0 # TODO: function call to evaluate the objective function
        lst_J.append(J)
        
        # Calculate new centroids from the clusters
        centroids = None # TODO: function call to recompute the centroids
        J = 0 # TODO: function call to evaluate the objective function again
        lst_J.append(J)
        
        if it > 0 and np.abs(lst_J[-1] - lst_J[-2]) < eps:
            print(f'Iteration {it+1}. Algorithm converged.')
            print(f'New centroids: {centroids}')
            break
    
    return ind_samples_clusters, centroids, lst_J

