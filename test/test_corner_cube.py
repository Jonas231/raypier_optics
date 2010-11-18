from raytrace.sources import ParallelRaySource
from raytrace.tracer import RayTraceModel
from raytrace.corner_cubes import HollowRetroreflector


source = ParallelRaySource(origin=(-10,0.1,50),
                           direction=(0,0,-1),
                           radius=4,
                           scale=0.1,
                           number=20)

cc = HollowRetroreflector()

model = RayTraceModel(sources=[source],
                      optics=[cc])

model.configure_traits()
#model.update = True
#print source.TracedRays