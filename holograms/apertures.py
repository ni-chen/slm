"""
Defines apertures that can be applied to holograms.
"""

def hori(hologram,center,width,return_center=False):
    """Applies a horizontal aperture onto the hologram and returns a copy. The
    center of the hologram will be moved away from the edges of the hologram so
    that the full width is always shown.
    
    Parameters:
        center: vertical center of the aperture (starting from the top)
        width: width of the aperture
    
    Returns:
        masked_holo: hologram masked with the virtual aperture
        center: horizontal center of the aperture (in case this has changed)
    """
    masked_holo = hologram.copy()
    if center < width/2:
        center = width/2
    if center > hologram.shape[0]-width/2:
        center = hologram.shape[0]-width/2
    start = int(round(center-width/2))
    end = int(round(center+width/2))
    if start < 0:
        start = 0
    masked_holo[:start,:] = 0
    masked_holo[end+1:,:] = 0
    if return_center:
        return masked_holo, center
    else:
        return masked_holo

def vert(hologram,center,width,return_center=False):
    """Applies a vertical aperature onto the hologram and returns a copy.

    Parameters:
        center: horizontal center of the aperture (starting from the left)
        width: width of the aperture
    
    Returns:
        masked_holo: hologram masked with the virtual aperture
        center: horizontal center of the aperture (in case this has changed)
    """
    masked_holo = hologram.copy()
    if center < width/2:
        center = width/2
    if center > hologram.shape[1]-width/2:
        center = hologram.shape[1]-width/2
    start = int(round(center-width/2))
    end = int(round(center+width/2))
    if start < 0:
        start = 0
    masked_holo[:,:start] = 0
    masked_holo[:,end+1:] = 0
    if return_center:
        return masked_holo, center
    else:
        return masked_holo

def circ(hologram,center=None,radius=None):
    """Applies a circular aperature onto the hologram and returns a copy.

    Parameters:
        center: tuple (x0,y0) containing the center of the aperture. None to 
                use the center of the hologram
        radius: radius of the aperture. None for the largest circular aperture
                that will fit on the display
    
    Returns:
        masked_holo: hologram masked with the virtual aperture
    """
    masked_holo = hologram.copy()
    if center is None:
        center = (hologram.shape[1]/2,hologram.shape[0]/2)
    if radius is None:
        radius = min(hologram.shape[1]-center[0],center[0],
                     hologram.shape[0]-center[1],center[1])
    for i in range(hologram.shape[0]):
        for j in range(hologram.shape[1]):
            if (i-center[1])**2+(j-center[0])**2 > radius**2:
                masked_holo[i,j] = 0
    return masked_holo