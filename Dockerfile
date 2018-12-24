FROM python:3.6
RUN pip install pandas matplotlib
RUN mkdir /home/data
RUN mkdir /home/data/RT60
RUN mkdir /home/src
RUN mkdir -p /root/.config/matplotlib
RUN echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc

COPY . /home
WORKDIR /home/src
CMD python rt_60.py
RUN ls -la /home
CMD tail -f /dev/null
