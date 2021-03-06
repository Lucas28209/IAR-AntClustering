from ant_clustering import AntClustering

''' AntClustering params:
             grid:int       - Grid size                 defaults to 100
             rad:int        - Ant radius                defaults to 2
             antnum:int     - # agents                  defaults to 50
             iterations:int - # iterations              defaults to 5*10**6
             fname:string   - Dataset file              defaults to '400.txt'
             alpha:float    - Alpha value               defaults to 0
             sleep:int      - Sleep ns before starting  defaults to 0
             dsize:int      - Display size              defaults to 500 '''

if __name__ == "__main__":
    antcluster = AntClustering(rad=3,
                               grid=50,
                               antnum=10,
                               fname='400.txt',
                               #alpha=1.3,
                               sleep=3,
                               iterations= 5*10**1)
    antcluster.run()
