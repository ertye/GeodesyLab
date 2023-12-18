clc 
close all
clear all

% 设置数据文件路径
FindPath = 'D:\Program Files\GeodesyLab-main\GeodesyLab-main\ExampleData1\';

% 初始化绘图
figure;
hold on;

% 数据处理和可视化循环
for i = 0:9
    switch i
        case 0
            data1 = readtable(strcat(FindPath, 'UWEV.PA.tenv3.txt'));
            label0 = 'Station UWEV';
        case 1
            data1 = readtable(strcat(FindPath, 'NPIT.PA.tenv3.txt'));
            label0 = 'Station NPIT';
        case 2
            data1 = readtable(strcat(FindPath, 'CNPK.PA.tenv3.txt'));
            label0 = 'Station CNPK';
        case 3
            data1 = readtable(strcat(FindPath, 'BYRL.PA.tenv3.txt'));
            label0 = 'Station BYRL';
        case 4
            data1 = readtable(strcat(FindPath, 'JOKA.PA.tenv3.txt'));
            label0 = 'Station JOKA';
        case 5
            data1 = readtable(strcat(FindPath, 'HNLC.PA.tenv3.txt'));
            label0 = 'Station HNLC';
        case 6
            data1 = readtable(strcat(FindPath, 'HILO.PA.tenv3.txt'));
            label0 = 'Station HILO';
        case 7
            data1 = readtable(strcat(FindPath, 'MANE.PA.tenv3.txt'));
            label0 = 'Station MANE';
        case 8
            data1 = readtable(strcat(FindPath, 'KOSM.PA.tenv3.txt'));
            label0 = 'Station KOSM';
        case 9
            data1 = readtable(strcat(FindPath, 'AHUP.PA.tenv3.txt'));
            label0 = 'Station AHUP';
    end

    % 提取数据
    Time = data1{:, 3};
    Latitude = data1{:, 9};
    Longitude = data1{:, 11};
    Height = data1{:, 13};

    % 数据标准化
    Latitude = Latitude - Latitude(1);
    Longitude = Longitude - Longitude(1);
    Height = Height - Height(1);

    % 数据平滑处理
    Latitude = smoothdata(Latitude, 'sgolay', 10);
    Longitude = smoothdata(Longitude, 'sgolay', 10);
    Height = smoothdata(Height, 'sgolay', 100);

    % 绘图
    subplot(3, 1, 1);
    plot(Time, Latitude, 'DisplayName', label0);
    ylabel('East(m)');
    hold on;

    subplot(3, 1, 2);
    plot(Time, Longitude, 'DisplayName', label0);
    ylabel('North(m)');
    hold on;

    subplot(3, 1, 3);
    plot(Time, Height, 'DisplayName', label0);
    xlabel('Time of observation (year)');
    ylabel('Height(m)');
    hold on;
end


% 添加图例
subplot(3, 1, 1);
legend;
subplot(3, 1, 2);
legend;
subplot(3, 1, 3);
legend;
hold off;
